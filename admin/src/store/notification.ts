import { ref } from 'vue';

export type Notification = {
  text: string;
  type: 'success' | 'error';
  isShown: boolean;
};

const notifications = ref<Notification[]>([]);
export const useNotificationStore = () => {
  const showNotification = (note: { text: string; type?: 'success' | 'error' }) => {
    notifications.value.push({
      type: 'success',
      ...note,
      isShown: true
    });
  };

  return {
    notifications,
    showNotification
  };
};
