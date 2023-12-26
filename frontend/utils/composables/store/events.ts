import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { loadableEmpty } from '~/utils/functions/loadable';

export type Event = {
  id: string;
  cover: string;
  date: string;
  name: string;
  url: string;
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
