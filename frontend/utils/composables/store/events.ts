import { useState } from '#app';
import { useRequest } from '~/utils/composables/useRequest';
import { Event } from '~/utils/types/events';
import { Loadable } from '~/utils/types';

export const useEventsStore = () => {
  const state = useState('events-state', () => ({
    events: Loadable<Event[]>,
  }));

  const getEvents = async () => {
    if (state.value.events.loaded) {
      return state.value.events;
    }

    const res = await useRequest<Event>('/events', {
      method: 'GET',
    });

    if (res.data) {
      state.value.events.data = res.data;
      state.value.events.loaded = true;
    }

    return state.value.events;
  };

  return {
    getEvents,
  };
};
