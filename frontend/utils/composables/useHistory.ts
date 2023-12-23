import { useRouter } from '#app';

export function useBack() {
  const $router = useRouter();

  const prevRoute = toRef(() => $router.options.history.state.back);
  const back = () => {
    if (prevRoute.value) {
      $router.back();
    } else {
      $router.push('/');
    }
  };

  return {
    back,
  };
}
