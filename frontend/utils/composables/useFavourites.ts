import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';

export const useFavourites = () => {
  const state = useState('favourites-state', () => ({}));

  const toggleFavourite = async (content_type: ContentType, content_id: number) => {
    const res = await useRequest('/save-content', {
      method: 'POST',
      body: {
        user_id: 1,
        content_type,
        content_id,
      },
    });

    console.log(res);
  };

  return {
    toggleFavourite,
  };
};
