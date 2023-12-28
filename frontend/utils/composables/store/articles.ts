import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';
import { useSpecialityStore } from '~/utils/composables/store/speciality';

export type Article = {
  id: number;
  article_name: string;
  cover: string;
};

export type ArticlePlump = {
  id: number;
  article_name: string;
  cover: string;
  access_number: string;
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
};

export const useArticlesStore = () => {
  const { speciality } = useSpecialityStore();

  const state = useState('acticles-store', () => ({
    articles: loadableEmpty<Article[]>([]),
  }));

  const getArticles = async () => {
    if (!state.value.articles.loaded && speciality.value) {
      const res = await useRequest<Article[]>(`/articles/specialty/${speciality.value.id}`, {
        method: 'GET',
      });

      if (res.data) {
        state.value.articles.data = res.data;
        state.value.articles.loaded = true;
      }
    }

    return state.value.articles;
  };

  const getArticle = async (id: number) => {
    const res = await useRequest<ArticlePlump>(`/articles/${id}`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getArticle,
    getArticles,
  };
};
