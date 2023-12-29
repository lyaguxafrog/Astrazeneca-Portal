import { useRoute, useRouter, useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export const useAuth = () => {
  const $router = useRouter();
  const $route = useRoute();

  const { speciality } = useSpecialityStore();

  const accessToken = useCookie('access-token');
  const userId = useCookie('user-id');

  const state = useState('auth-state', () => ({
    userId: userId.value ? +userId.value : 0,
  }));

  const toLogin = async () => {
    const res = await useRequest<{
      sso_signin_url: string;
    }>('/sso/signin/', {
      method: 'GET',
    });

    if (res.data) {
      window.open(res.data.sso_signin_url, '_self');
    }
  };

  const sendAuthToken = async () => {
    const userIdCookie = useCookie('user-id');

    const token = $route.query.access_token;
    const refresh = $route.query.refresh;

    if (token && speciality.value) {
      const res = await useRequest<{
        user_id: number;
      }>('/create_user/', {
        method: 'POST',
        body: {
          temporary_token: token,
          specialty_id: speciality.value.id,
        },
      });

      if (res.data) {
        userIdCookie.value = `${res.data.user_id}`;
        state.value.userId = res.data.user_id;
      }

      $router.replace({
        query: {
          ...$route.query,
          access_token: undefined,
          refresh: undefined,
        },
      });
    }
  };

  return {
    toLogin,
    sendAuthToken,

    token: '123',
    userId: toRef(() => state.value.userId),
  };
};
