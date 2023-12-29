import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { loadableEmpty } from '~/utils/functions/loadable';
import { ArticlePlump } from '~/utils/composables/store/articles';

export type VideoContentType = 'видеолекция' | 'кейс';

export type Video = {
  id: number;
  video_article_url: string;
  video: string;
  video_cover_url: string;
  conspect: string;
  access_number: string;
  content_type: VideoContentType;
};

export type VideoPlump = {
  id: number;
  video_article: string;
  video: string;
  video_cover: string;
  conspect: string;
  access_number: string;
  content_type: VideoContentType;
  video_recomendations: number[];
};

export const useVideosStore = () => {
  const state = useState('videos-state', () => ({
    videos: loadableEmpty<Video[]>([]),
  }));

  const { speciality } = useSpecialityStore();

  const getVideos = async () => {
    if (!state.value.videos.loaded && speciality.value?.id) {
      const res = await useRequest<Video[]>(`/video-lectures/speciality/${speciality.value.id}`, {
        method: 'GET',
      });

      if (res.data) {
        state.value.videos.data = res.data;
        state.value.videos.loaded = true;
      }
    }

    return state.value.videos.data;
  };

  const getVideo = async (id: number) => {
    const res = await useRequest<Video>(`/video-lectures/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getVideos,
    getVideo,
  };
};
