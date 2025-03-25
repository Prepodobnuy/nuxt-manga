import { defineStore } from 'pinia';


const searchEntities = {
    0: 'title',
    1: 'person',
    2: 'user',
}

export const useSearchStore = defineStore('search', () => {
    const state = reactive({
        searchIndex: 0,
        prompt: '',
        users: [],
        persons: [],
        titles: [],
    });

    return state
});