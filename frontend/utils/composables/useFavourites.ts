import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';
import { useAuth } from '~/utils/composables/useAuth';

export const useFavourites = () => {
  const { userId } = useAuth();

  const state = useState('favourites-state', () => ({}));

  const toggleFavourite = async (contentType: ContentType, contentId: number) => {
    const res = await useRequest('/save-content/', {
      method: 'POST',
      body: {
        user_id: userId.value,
        content_type: contentType,
        content_id: contentId,
      },
    });

    console.log(res);
  };
  const getFavourites = async () => {
    const res = await useRequest(`/save-content/get/${userId.value}`, {
      method: 'POST',
    });

    console.log(res);
  };

  return {
    toggleFavourite,

    getFavourites,
  };
};
