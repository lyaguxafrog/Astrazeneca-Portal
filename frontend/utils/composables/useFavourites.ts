import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';

export const useFavourites = () => {
  const state = useState('favourites-state', () => ({}));

  const toggleFavourite = async (contentType: ContentType, contentId: number) => {
    const res = await useRequest('/save-content', {
      method: 'POST',
      body: {
        user_id: 1,
        content_type: contentType,
        content_id: contentId,
      },
    });

    console.log(res);
  };

  return {
    toggleFavourite,
  };
};
