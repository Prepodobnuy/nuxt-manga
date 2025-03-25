import { defineStore } from 'pinia';


export const useCreatePersonStore = defineStore('create-person', () => {
    const state = reactive({
        image: null,
        ruName: null,
        enName: null,
        orName: null,
        type: null,
    });

    const attention = reactive({
        image: false,
        ruName: false,
        enName: false,
        orName: false,
        type: false,
    })

    const postForm = () => {
        for (const key in state) {
            if (state[key as keyof typeof state] == null) {
                attention[key as keyof typeof attention] = true;
            } else {
                attention[key as keyof typeof attention] = false;
            }
        }
    
        if (Object.values(attention).every((val) => !val)) {
            console.log('Форма отправлена:', state);
        } else {
            console.error('Пожалуйста, заполните все поля');
        }
      };

    return {
        state,
        attention,
        postForm,
    }
});