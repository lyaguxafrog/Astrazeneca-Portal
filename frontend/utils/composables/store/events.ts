import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Event = {
  id: number;
  date: string;
  name: string;
  url: string;
  cover: string;
  image_desktop_1400px: string;
  image_desktop_570px: string;
  image_mobile_540px: string;
  image_mobile_270px: string;
};
export const useEventsStore = () => {
  const state = useState('events-state', () => ({
    events: loadableEmpty<Event[]>(),
  }));

  const getEvents = async () => {
    if (!state.value.events.loaded) {
      const res = await useRequest<Event[]>('/events', {
        method: 'GET',
      });

      if (res.data) {
        state.value.events.data = res.data;
        state.value.events.loaded = true;
      }
    }

    return state.value.events;
  };

  return {
    getEvents,
  };
};
