import { toRef, computed } from 'vue';
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
  const specialityCookie = useCookie(specialityCookieName);

  const state = useState('speciality', () => ({
    specialities: loadableEmpty<Speciality[]>([]),
    specialityId: specialityCookie.value ? +specialityCookie.value : undefined,
    speciality: undefined as Speciality | undefined,
  }));

  const init = async () => {
    const specialityCookie = await useCookie(specialityCookieName);

    state.value.specialityId = specialityCookie.value ? +specialityCookie.value : undefined;
  };

  const getSpecialities = async () => {
    if (!state.value.specialities.loaded) {
      const res = await useRequest<Speciality[]>('/specialty', {
        method: 'GET',
        ignoreError: true,
      });


      if (res.data) {
        state.value.specialities.data = res.data;
        state.value.specialities.loaded = true;
      }
    }

    return state.value.specialities.data;
  };

  const setSpeciality = async (id: number) => {
    const specialityCookie = await useCookie(specialityCookieName);

    state.value.specialityId = id;
    specialityCookie.value = `${id}`;
  };

  return {
    specialities: toRef(() => state.value.specialities),
    specialityId: toRef(() => state.value.specialityId),
    speciality: computed(() => {
      return state.value.specialities.data?.find((s) => s.id === state.value.specialityId);
      }
    ),

    init,
    setSpeciality,
    getSpecialities,
  };
}
