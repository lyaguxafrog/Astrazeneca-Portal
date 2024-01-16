import { useState } from '#app';
import { toRef } from 'vue';
import { useRequest } from '~/utils/composables/useRequest';
import { useSpecialityStore } from '~/utils/composables/store/speciality';
import { loadableEmpty } from '~/utils/functions/loadable';
import { ArticlePlump } from '~/utils/composables/store/articles';

export enum VideoContentType {
  Video = 'lecture',
  Case = 'case',
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
    title: string;
    recomendation_cover_desktop_500px: string;
    recomendation_cover_desktop_1000px: string;
    recomendation_cover_mobile_280px: string;
    recomendation_cover_mobile_560px: string;
  }[];
};

export const useVideosStore = () => {
  const state = useState('videos-state', () => ({
    videos: loadableEmpty<Video[]>([]),
  }));

  const { specialityId } = useSpecialityStore();

  const getVideos = async (force?: boolean) => {
    const loadAll = sessionStorage.getItem('showAllContent');

    let url = '/video-lectures';

    if (!loadAll) {
      url += `/speciality/${specialityId.value}`;
    }

    if ((!state.value.videos.loaded && specialityId.value) || force) {
      const res = await useRequest<Video[]>(url, {
        method: 'GET',
      });

      if (res.data) {
        state.value.videos.data = res.data;
        state.value.videos.loaded = true;
      }
    }
  };

  const getVideo = async (id: number) => {
    const res = await useRequest<VideoPlump>(`/video-lectures/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    videos: toRef(() => state.value.videos.data),

    getVideos,
    getVideo,
  };
};
