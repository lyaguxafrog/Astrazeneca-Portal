const buildFormData = (formData: any, obj: any, parentKey = '', parentIndex = 0) => {
  if (Array.isArray(obj)) {
    obj.forEach((element, index) => {
      buildFormData(formData, element, parentKey, index);
    });
  } else if (obj && typeof obj === 'object' && !(obj instanceof File)) {
    Object.keys(obj).forEach((key) => {
      buildFormData(formData, obj[key], parentKey ? `${parentKey}[${parentIndex}][${key}]` : key);
    });
  } else {
    if (obj == null) {
      return;
    }

    const value = typeof obj === 'number' || typeof obj === 'boolean' ? obj.toString() : obj;
    formData.append(parentKey, value);
  }
};

export const objectToFormData = (obj: any) => {
  const formData = new FormData();
  buildFormData(formData, obj);

  return formData;
};

function processFormData(body: Record<string, any>) {
  const fd = new FormData();

  for (const key in body) {
    if (body[key]) {
      const item = body[key];

      if (Array.isArray(item)) {
        for (let i = 0; i < item.length; i += 1) {
          if (typeof item[i] === 'object') {
            fd.append(key, JSON.stringify(item[i]));
          } else {
            fd.append(key, item[i]);
          }
        }

        continue;
      }

      if (typeof item === 'object' && !((item as any) instanceof File)) {
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
        body = objectToFormData(options.body);
      } else {
        body = JSON.stringify(body);
      }
    }

    try {
      const req = await fetch(`https://astraportal.dev-demo.online/api${url}`, {
        method: options.method,
        body: body as BodyInit | null | undefined,
        headers: !options.formData
          ? {
              'Content-type': 'application/json'
            }
          : undefined
      }).then((res) => {
        if (res.status !== 204) {
          return res.json();
        }

        return undefined;
      });

      return req;
    } catch (e) {
      console.error(e);
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

  const put = <T>(url: string, data: any, formData?: boolean): Promise<T> =>
    request(url, {
      method: 'PUT',
      body: data,
      formData
    });

  const del = <T>(url: string): Promise<T> =>
    request(url, {
      method: 'DELETE'
    });

  return {
    get,
    post,
    put,
    del
  };
};
