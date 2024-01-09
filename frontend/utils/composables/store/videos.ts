import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { loadableEmpty } from '~/utils/functions/loadable';
import { ArticlePlump } from '~/utils/composables/store/articles';

export enum VideoContentType {
  Video = 'видеолекция',
  Case = 'кейс',
}

export type Video = {
  id: number;
  video_article_url: string;
  video: string;
  video_cover_url: string;
  video_cover_desktop_2800px: string;
  video_cover_desktop_1400px: string;
  video_cover_mobile_840px: string;
  video_cover_mobile_420px: string;
  conspect: string;
  access_number: string;
  content_type: VideoContentType;
};

export type VideoPlump = {
  id: number;
  video_article: string;
  video_url: string;
  video_cover_desktop_2800px: string;
  video_cover_desktop_1400px: string;
  video_cover_mobile_840px: string;
  video_cover_mobile_420px: string;
  video_cover: string;
  conspect: string;
  access_number: string;
  content_type: VideoContentType;
  video_recomendations?: {
    id: number;
    preview: string;
    title: string;
  }[];
};

export const useVideosStore = () => {
  const state = useState('videos-state', () => ({
    videos: loadableEmpty<Video[]>([]),
  }));

  const { specialityId } = useSpecialityStore();

  const getVideos = async () => {
    if (!state.value.videos.loaded && specialityId.value) {
      const res = await useRequest<Video[]>(`/video-lectures/speciality/${specialityId.value}`, {
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
    const res = await useRequest<VideoPlump>(`/video-lectures/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getVideos,
    getVideo,
  };
};
