import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { ContentType } from '~/utils/types';
import { VideoPlump } from '~/utils/composables/store/videos';
import { useAuth } from '~/utils/composables/useAuth';
import { loadableEmpty } from '~/utils/functions/loadable';

type FavImages = {
  favorite_desktop_300px?: string;
  favorite_desktop_600px?: string;
  favorite_mobile_500px?: string;
  favorite_mobile_250px?: string;

  favorite_desktop_120px?: string;
  favorite_desktop_280px?: string;
  favorite_mobile_140px?: string;
  favorite_mobile_70x?: string;
}

export type Favourites = {
  [ContentType.Video]?: ({ content_type: string } & FavImages)[];
  [ContentType.Article]?: ({ article_name: string } & FavImages)[];
  [ContentType.Stories]?: ({ title: string } & FavImages)[];
};

export const useFavourites = () => {
  const { userId } = useAuth();

  const state = useState('favourites-state', () => ({
    favourites: loadableEmpty<Favourites>(),
  }));

  const getFavourites = async () => {
    if (!userId.value) {
      return;
    }

    const res = await useRequest<{ saved_content: Favourites }>(
      `/save-content/get/${userId.value}`,
      {
        method: 'GET',
        ignoreError: true,
      }
    );

    if (res.data) {
      state.value.favourites.data = res.data.saved_content;
      state.value.favourites.loaded = true;
    }
  };
  const toggleFavourite = async (contentType: ContentType, contentId: number) => {
    if (!isInFavourite(contentType, contentId)) {
      await useRequest('/save-content/', {
        method: 'POST',
        body: {
          user_id: userId.value,
          content_type: contentType,
          content_id: contentId,
        },
      });
    } else {
      await useRequest('/save-content/remove/', {
        method: 'DELETE',
        body: {
          user_id: userId.value,
          content_type: contentType,
          content_id: contentId,
        },
      });
    }

    await getFavourites();
  };

  const isInFavourite = (contentType: ContentType, contentId: number) => {
    return state.value.favourites?.data?.[contentType]?.find((f) => f.id === contentId);
  };

  return {
    isInFavourite,
    toggleFavourite,

    getFavourites,
    favourites: toRef(() => state.value.favourites),
  };
};
