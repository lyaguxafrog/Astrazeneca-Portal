import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type Article = {
  id: number;
  article_name: string;
  cover_desktop_1400px: string;
  cover_desktop_2800px: string;
  cover_mobile_420px: string;
  cover_mobile_840px: string;
  information: string;
};

export type ArticlePlump = {
  id: number;
  article_name: string;
  cover: string;
  access_number: string;
  first_abzac: string;
  article_type: 'статья';
  content_blocks: [
    {
      id: number;
      image: string | null;
      content_type: 'text' | 'quote' | 'text_with_image';
      order: number;
      text: string;
    }
  ];
  final_content?: string;
  main_cover_desktop_3200px?: string;
  main_cover_desktop_1600px?: string;
  main_cover_desktop_720px?: string;
  main_cover_desktop_360px?: string;
};

export const useArticlesStore = () => {
  const { specialityId } = useSpecialityStore();

  const state = useState('acticles-store', () => ({
    articles: loadableEmpty<Article[]>([]),
  }));

  const getArticles = async () => {
    if (!state.value.articles.loaded && specialityId.value) {
      const res = await useRequest<Article[]>(`/articles/specialty/${specialityId.value}`, {
        method: 'GET',
      });

      if (res.data) {
        state.value.articles.data = res.data;
        state.value.articles.loaded = true;
      }
    }
  };

  const getArticle = async (id: number) => {
    const res = await useRequest<ArticlePlump>(`/articles/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    articles: toRef(() => state.value.articles),

    getArticle,
    getArticles,
  };
};
