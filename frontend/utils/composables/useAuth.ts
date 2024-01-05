import { useRoute, useRouter, useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useHistoriesStore } from '~/utils/composables/store/histories';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export const useAuth = () => {
  const $router = useRouter();
  const $route = useRoute();
  const historiesStore = useHistoriesStore();

  const { speciality, setSpeciality } = useSpecialityStore();

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

  const checkAccessToken = async () => {
    const userIdCookie = useCookie('user-id');

    const token = $route.query.access_token;

    if (!token) {
      return;
    }

    try {
      const res = await useRequest<{
        user_id: number;
        specialty: number;
      }>(`/get_user/${token}`, {
        method: 'GET',
      });

      if (res.data?.user_id) {
        userIdCookie.value = `${res.data.user_id}`;
        state.value.userId = res.data.user_id;
        setSpeciality(res.data.specialty);

        await $router.replace({
          query: {
            ...$route.query,
            access_token: undefined,
            refresh: undefined,
          },
        });
      } else {
        setSpeciality(0);
      }
    } catch (e) {
      console.error(e);
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
          specialty: speciality.value.id,
        },
      });

      if (res.data) {
        userIdCookie.value = `${res.data.user_id}`;
        state.value.userId = res.data.user_id;
      }

      await $router.replace({
        query: {
          ...$route.query,
          access_token: undefined,
          refresh: undefined,
        },
      });

      await historiesStore.getHistories(true);
    }
  };

  return {
    toLogin,
    sendAuthToken,
    checkAccessToken,

    token: '123',
    userId: toRef(() => state.value.userId),
  };
};
