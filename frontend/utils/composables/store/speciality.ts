import { toRef } from 'vue';
import { useCookie } from '#app';
import { loadableEmpty, Loadable } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';

const specialityCookieName = 'selected-speciality';

type Speciality = {
  id: number;
};

export function useSpecialityStore() {
  const specialityCookie = useCookie(specialityCookieName);
  const state = useState('speciality', () => ({
    specialities: loadableEmpty<Speciality[]>(),
    speciality: specialityCookie.value,
  }));

  const getSpecialities = async () => {
    if (state.value.specialities.loaded) {
      return state.value.specialities.data;
    }

    const res = await useRequest<Speciality[]>('/', {
      method: 'GET',
    });

    if (res.data) {
      state.value.specialities.data = res.data;
      state.value.specialities.loaded = true;
    }
  };

  const setSpeciality = (id: string) => {
    const specialityCookie = useCookie(specialityCookieName);
    state.value.speciality = specialityCookie.value = id;
  };

  const specialities = [
    {
      id: '1',
      name: 'Патоморфолог',
      img: '/img/specialities/DNA.png',
    },
    {
      id: '2',
      name: 'Радиотерапевт',
      img: '/img/specialities/MRI.png',
    },
    {
      id: '3',
      name: 'Хирург',
      img: '/img/specialities/SCALPEL.png',
    },
    {
      id: '4',
      name: 'Химиотерапевт',
      img: '/img/specialities/chemytherapy.png',
    },
  ];

  return {
    specialities,
    speciality: toRef(() => state.value.speciality),

    setSpeciality,
    getSpecialities,
  };
}
