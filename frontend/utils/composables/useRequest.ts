import { /* useLazyAsyncData, */ useAsyncData, useRuntimeConfig, createError } from '#app';
import { useAuth } from '~/utils/composables/useAuth';

export type Method = 'GET' | 'DELETE' | 'OPTIONS' | 'POST' | 'PUT' | 'PATCH';

type ApiError = {
  data: {
    status: number;
    violations: [
      {
        id: string;
        title: string;
      }
    ];
  };
};

export type Metadata = {
  current: number;
  pagesCount: number;
  elementsCount: number;
  next: number;
  previous: number;
};

type RequestConfig = {
  method: Method;
  authRequired?: boolean;
  lazy?: boolean;
  key?: string;
  body?: Record<string, unknown> | FormData;
  params?: Record<string, unknown>;
  headers?: Record<string, string>;
  noteIfError?: boolean;
};

export const getRequestKey = (
  url: string,
  config: {
    body?: RequestConfig['body'];
    params?: RequestConfig['params'];
    key?: RequestConfig['key'];
  }
) =>
  url +
  JSON.stringify(config.body || '') +
  JSON.stringify(config.params || '') +
  (config.key || '');

export async function useRequest<Res = unknown>(url: string, config: RequestConfig) {
  const { apiUrl } = useRuntimeConfig().public;

  const { token } = useAuth();

  const headers = config.headers || {};
  headers['content-type'] = 'application/json';
  if (config.authRequired) {
    headers.Authorization = `Bearer ${token.value}`;
  }

  const fetchConfig = {
    baseURL: apiUrl,
    method: config.method,
    params: config.params,
    body: JSON.stringify(config.body),
    lazy: config.lazy,
    // key: url + JSON.stringify(config.body) + JSON.stringify(config.params) + config.key, // уникальный ключ, чтобы избежать кеширования с другими запросами,
    key: getRequestKey(url, {
      body: config.body,
      params: config.params,
      key: config.key,
    }),
    headers,
  };

  /* const fetchMethod = config.lazy ? useLazyAsyncData : useAsyncData; */

  const fetchMethod = useAsyncData;

  const { data, pending, refresh, error } = await fetchMethod(url, () => $fetch(url, fetchConfig));

  if (error?.value?.statusCode === 404 || error?.value?.statusCode === 500) {
    throw createError({
      statusCode: 404,
      statusMessage: 'Page Not Found',
    });
  }

  return {
    // @ts-ignore
    data: (data.value?.data ? data.value?.data : data.value) as Res | undefined,
    // убрать эту фигню - она тут потому что изменился бэк
    metadata: (data.value?.metadata ? data.value?.metadata : undefined) as Metadata | undefined,
    pending,
    refresh,
    error: error.value as ApiError | null,
  };
}
