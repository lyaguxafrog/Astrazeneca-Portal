import { useRouter } from '#app';

export function useBack() {
  const $router = useRouter();

  const prevRoute = toRef(() => $router.options.history.state.back);
  const back = async () => {
    if (prevRoute.value) {
      await $router.back();
    } else {
      await $router.push('/');
    }
  };

  return {
    back,
  };
}
