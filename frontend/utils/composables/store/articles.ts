import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';

export type Article = {
  id: number;
  article_name: string;
};

export const useArticlesStore = () => {
  const state = useState('acticles-store', () => ({}));

  const getArticle = async (id: number) => {
    const res = await useRequest<Article>(`/article/${id}/`, {
      method: 'GET',
    });

    return res.data;
  };

  return {
    getArticle,
  };
};
