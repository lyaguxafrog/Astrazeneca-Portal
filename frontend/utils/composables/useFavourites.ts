import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';
import { useAuth } from '~/utils/composables/useAuth';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Favourite = {
  content_type: ContentType;
  content_id: number;
};

export const useFavourites = () => {
  const { userId } = useAuth();

  const state = useState('favourites-state', () => ({
    favourites: loadableEmpty<Favourite[]>([]),
  }));

  const toggleFavourite = async (contentType: ContentType, contentId: number) => {
    const res = await useRequest('/save-content/', {
      method: 'POST',
      body: {
        user_id: userId.value,
        content_type: contentType,
        content_id: contentId,
      },
    });

    if (res.data) {
      state.value.favourites.data?.push({
        content_type: contentType,
        content_id: contentId,
      });
    }
  };

  const getFavourites = async () => {
    const res = await useRequest(`/save-content/get/${userId.value}`, {
      method: 'GET',
    });

    console.log(res);
  };

  const isInFavourite = (contentType: ContentType, contentId: number) => {
    return !!state.value.favourites.data?.find(
      (f) => f.content_type === contentType && f.content_id === contentId
    );
  };

  return {
    isInFavourite,
    toggleFavourite,

    getFavourites,
  };
};
