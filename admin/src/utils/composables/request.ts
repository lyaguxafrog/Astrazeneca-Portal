function processFormData(body: Record<string, any>) {
  const fd = new FormData();

  for (const key in body) {
    if (body[key]) {
      const item = body[key];

      if (Array.isArray(item)) {
        for (let i = 0; i < item.length; i += 1) {
          fd.append(`${key}[]`, item[i]);
        }

        continue;
      }

      if (typeof item === 'object' && (!item as any) instanceof File) {
        fd.append(key, JSON.stringify(item));
      } else {
        fd.append(key, item);
      }
    }
  }

  return fd;
}

export const useRequest = () => {
  const request = async (
    url: string,
    options: {
      method: 'GET' | 'POST' | 'PUT' | 'DELETE';
      body?: Record<string, any>;
      formData?: boolean;
    }
  ) => {
    let body: Record<string, any> | string | undefined = options.body
      ? { ...options.body }
      : undefined;

    if (options.body) {
      if (options.formData) {
        body = processFormData(options.body);
      } else {
        body = JSON.stringify(body);
      }
    }

    try {
      const req = await fetch(`https://astraportal.dev-demo.online/api${url}`, {
        method: options.method,
        body: body as BodyInit | null | undefined
      }).then((res) => res.json());

      return req;
    } catch (e) {
      console.log(e);
      throw e;
    }
  };

  const get = <T>(url: string): Promise<T> =>
    request(url, {
      method: 'GET'
    });

  const post = <T>(url: string, data: any, formData?: boolean): Promise<T> =>
    request(url, {
      method: 'POST',
      body: data,
      formData
    });

  const put = (url: string) => {
    console.log(url);
    return request(url, {
      method: 'POST'
    });
  };

  return {
    get,
    post,
    put
  };
};
