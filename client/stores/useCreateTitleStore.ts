import { defineStore } from 'pinia';


export const useCreateTitleStore = defineStore('create-title', () => {
    const state = reactive({
        image: null,
        ruName: null,
        enName: null,
        orName: null,
        anName: null,
        description: null,

        trStatus: null,
        rlStatus: null,
        type: null,

        ageRating: null,
        releaseYear: null,

        tags: [],
        genres: [],

        authorId: null,
        artistId: null,
        publisherId: null,
    });

    const attention = reactive({
        image: false,
        ruName: false,
        enName: false,
        orName: false,
        anName: false,
        description: false,

        trStatus: false,
        rlStatus: false,
        type: false,
        
        ageRating: false,
        releaseYear: false,
        
        tags: false,
        genres: false,
        
        authorId: false,
        artistId: false,
        publisherId: false,
    })

    const compare = reactive({
        image: () => state.image === null ,
        ruName: () => state.ruName === null || state.ruName === '',
        enName: () => state.enName === null || state.enName === '',
        orName: () => state.orName === null || state.orName === '',
        anName: () => state.anName === null || state.anName === '',
        description: () => state.description === null || state.description === '',
        trStatus: () => state.trStatus === null || ![0, 1, 2, 3].includes(state.trStatus),
        rlStatus: () => state.rlStatus === null || ![0, 1, 2, 3].includes(state.rlStatus),
        type: () => state.type === null || ![0, 1, 2].includes(state.type),
        ageRating: () => state.ageRating === null || ![0, 1, 2, 3].includes(state.ageRating),
        releaseYear: () => state.releaseYear === null || state.releaseYear === '',
        tags: () => JSON.stringify(state.tags) === JSON.stringify([]),
        genres: () => JSON.stringify(state.genres) === JSON.stringify([]),
        authorId: () => state.authorId === null,
        artistId: () => state.artistId === null,
        publisherId: () => state.publisherId === null,
    })

    const postForm = () => {
        for (const key in state) {
            attention[key as keyof typeof attention] = compare[key as keyof typeof compare]()
        }
    
        if (Object.values(attention).every((val) => !val)) {
            console.log('Форма отправлена:', state);
        }
      };

    return {
        state,
        attention,
        postForm,
    }
});