import { ref } from 'vue';
import { History } from '~/utils/types/histories';
export const useHistoriesStore = () => {
  const histories = ref<History[]>([
    {
      id: '1',
      url: '/videos/IMG_6650.MOV',
      preview: '/img/IMG_6650_Moment.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/1',
      color: '#00D1FF',
    },
    {
      id: '2',
      url: '/videos/IMG_6651.MOV',
      preview: '/img/IMG_6651_Moment.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/2',
      color: '#00D1FF',
    },
    {
      id: '3',
      url: '/videos/A_large_rock_waterfall.mp4',
      preview: '/img/photo_2023-12-11_19-13-51.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/3',
      color: '#E130FF',
    },
    {
      id: '4',
      url: '/videos/IMG_6650.MOV',
      preview: '/img/IMG_6650_Moment.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/4',
      color: '#00D1FF',
    },
    {
      id: '5',
      url: '/videos/IMG_6650.MOV',
      preview: '/img/IMG_6650_Moment.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/5',
      color: '#00D1FF',
    },
    {
      id: '6',
      url: '/videos/IMG_6650.MOV',
      preview: '/img/IMG_6650_Moment.jpg',
      avatar: '/img/avatar.jpg',
      name: 'Lorem ipsum',
      link: '/video/6',
      color: '#00D1FF',
    },
  ]);

  return {
    histories,
  };
};
