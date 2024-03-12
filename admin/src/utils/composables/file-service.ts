import { useRequest } from '@/utils/composables/request';
import { useNotificationStore } from '@/store/notification';

export const useFileService = () => {
  const { post } = useRequest();
  const { showNotification } = useNotificationStore();

  const loadFile = async (file: File) => {
    try {
      const res = await post<{
        file: string;
      }>(
        '/file/temp/',
        {
          file
        },
        true
      );

      return res?.file || '';
    } catch (e) {
      showNotification({
        text: 'Не удалось загрузить картинку',
        type: 'error'
      });
    }
  };

  return {
    loadFile
  };
};
