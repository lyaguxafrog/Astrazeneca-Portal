import { ref } from 'vue';

const notifications = ref<Notification[]>([]);
export const useNotificationStore = () => {
  const showNotification = (note: { text: string; type?: 'success' | 'error' }) => {
    notifications.value.push({
      type: 'success',
      ...note
    });
  };

  return {
    notifications,
    showNotification
  };
};

export type Notification = {
  text: string;
  type: 'success' | 'error';
};
