import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type Video = {
  id: number;
  video_article: string;
  video: string;
  video_cover: string;
  conspect: string;
  access_number: string;
};

export const useVideosStore = () => {
  const state = useState('videos-state', () => ({
    videos: [] as Video[],
    videosLoaded: false,
  }));

  const { speciality } = useSpecialityStore();

  const getVideos = async () => {
    if (!state.value.videosLoaded && speciality.value?.id) {
      const res = await useRequest(`/video-lectures/${speciality.value.name}`, {
        method: 'GET',
      });

      console.log(res);
    }

    return state.value.videos;
  };

  const getVideo = async (id: number) => {
    const res = await useRequest<Video>(`/video-lectures/${id}/`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getVideos,
    getVideo,
  };
};
