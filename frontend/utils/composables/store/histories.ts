import { loadableEmpty } from '~/utils/functions/loadable';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type History = {
  id: number;
  title: string;
  avatar: string;
  avatar_desktop_120px: string;
  avatar_desktop_280px: string;
  avatar_desktop_70px: string;
  avatar_desktop_140px: string;
  cover_image: string;
  cover_450px: string;
  cover_900px: string;
  is_active: boolean;
  link_to_page: string;
  video: string;
  color: string | null;
  specialties: number[];
};

export const useHistoriesStore = () => {
  const { specialityId } = useSpecialityStore();

  const state = useState('histories-state', () => ({
    histories: loadableEmpty<History[]>([]),
  }));

  const getHistories = async (force?: boolean) => {
    let url = '/stories';

    if (specialityId.value) {
      url += `/${specialityId.value}`;
    }

    if (!state.value.histories.loaded || force) {
      const res = await useRequest<History[]>(url, {
        method: 'GET',
      });

      if (res.data) {
        state.value.histories.data = res.data.reverse();
        state.value.histories.loaded = true;
      }
    }
  };

  return {
    histories: toRef(() => state.value.histories.data),

    getHistories,
  };
};
