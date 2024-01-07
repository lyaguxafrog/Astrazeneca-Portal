import { toRef } from 'vue';
import { useCookie } from '#app';
import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';

const specialityCookieName = 'selected-speciality';

type Speciality = {
  id: number;
  name: string;
  image_url: string;
  pro: string;
};

export function useSpecialityStore() {
  const state = useState('speciality', () => ({
    specialities: loadableEmpty<Speciality[]>(),
    speciality: undefined as number | undefined,
  }));

  const init = () => {
    const specialityCookie = useCookie(specialityCookieName);

    console.log(specialityCookie.value);

    state.value.speciality = specialityCookie.value ? +specialityCookie.value : undefined;
  };

  const getSpecialities = async () => {
    if (!state.value.specialities.loaded) {
      const res = await useRequest<Speciality[]>('/specialty', {
        method: 'GET',
      });

      if (res.data) {
        state.value.specialities.data = res.data;
        state.value.specialities.loaded = true;
      }
    }

    return state.value.specialities.data;
  };

  const setSpeciality = (id: number) => {
    const specialityCookie = useCookie(specialityCookieName);

    state.value.speciality = id;
    specialityCookie.value = `${id}`;
  };

  return {
    specialities: toRef(() => state.value.specialities),
    speciality: toRef(() =>
      state.value.specialities.data?.find((s) => s.id === state.value.speciality)
    ),

    init,
    setSpeciality,
    getSpecialities,
  };
}
