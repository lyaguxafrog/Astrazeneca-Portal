import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';
import { useAuth } from '~/utils/composables/useAuth';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Favourite = {
  id: number;
  content_type: ContentType;
  content_id: number;
};

export const useFavourites = () => {
  const { userId } = useAuth();

  const state = useState('favourites-state', () => ({
    favourites: loadableEmpty<Favourite[]>([]),
  }));

  const toggleFavourite = async (contentType: ContentType, contentId: number) => {
    if (!isInFavourite(contentType, contentId)) {
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
    } else {
      console.log({
        user_id: userId.value,
        content_type: contentType,
        content_id: contentId,
      });
      const res = await useRequest('/save-content/remove/', {
        method: 'DELETE',
        body: {
          user_id: userId.value,
          content_type: contentType,
          content_id: contentId,
        },
      });

      if (res.data) {
        state.value.favourites.data = state.value.favourites.data?.filter(
          (f) => f.content_type !== contentType && f.content_id !== contentId
        );
      }
    }
  };

  const getFavourites = async () => {
    if (state.value.favourites.loaded) {
      return;
    }

    const res = await useRequest<{ saved_content: Favourite[] }>(
      `/save-content/get/${userId.value}`,
      {
        method: 'GET',
      }
    );

    if (res.data) {
      state.value.favourites.data = res.data.saved_content;
      state.value.favourites.loaded = true;
    }
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
    favourites: toRef(() => state.value.favourites),
  };
};
