export const useRequest = () => {
  const request = async (
    url: string,
    options: {
      method: 'GET' | 'POST' | 'PUT' | 'DELETE';
      body?: FormData | string;
    }
  ) =>
    fetch(`https://astraportal.dev-demo.online/api${url}`, {
      method: options.method,
      body: options.body
    }).then((res) => res.json());

  const get = <T>(url: string): Promise<T> =>
    request(url, {
      method: 'GET'
    });

  const post = (url: string, data: any) =>
    request(url, {
      method: 'POST',
      body: JSON.stringify(data)
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
