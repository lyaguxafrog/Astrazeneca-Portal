import { useState } from '#app';
import { Video } from '~/utils/types/videos';
import { useRequest } from '~/utils/composables/useRequest';

export const useVideosStore = () => {
  const state = useState('videos-state', () => ({
    videos: [] as Video[],
    videosLoaded: false,
  }));

  const getVideos = async () => {
    if (state.value.videosLoaded) {
      return state.value.videos;
    }

    const res = await useRequest('/events', {
      method: 'GET',
    });

    console.log(res);
  };

  return {
    getVideos,
  };
};
