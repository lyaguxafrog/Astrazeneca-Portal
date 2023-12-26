import { useRequest } from '~/utils/composables/useRequest';

export const useAuth = () => {

  const toLogin = async () => {
    const res = await useRequest<{
      login_link: string,
    }>('/sso/login-link/', {
      method: 'GET',
    });

    if (res.data) {
      //window.open(res.data.login_link, '_self');
    }
  };
  return {
    toLogin,
    token: '123',
  };
};
