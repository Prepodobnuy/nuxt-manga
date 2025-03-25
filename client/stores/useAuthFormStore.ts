import { defineStore } from 'pinia';
import Login from '~/pages/auth/login.vue';


export const useAuthFormStore = defineStore('auth-form', () => {
    const state = reactive({
        login: '',
        password: '',
        email: '',
    });

    const attention = reactive({
        login: false,
        password: false,
        email: false,
    });

    const postLogin = () => {
        let valid = true;
        if (!(state.login.length > 4 && state.login.length < 20)) {
            attention.login = true;
            valid = false;
        }
        if (!(state.password.length > 4 && state.password.length < 20)) {
            attention.password = true;
            valid = false;
        }

        if (valid) {
            // api login here
        }
    }

    const postSignup = () => {
        let valid = true;
        if (!(state.login.length > 4 && state.login.length < 20)) {
            attention.login = true;
            valid = false;
        }
        if (!(state.password.length > 4 && state.password.length < 20)) {
            attention.password = true;
            valid = false;
        }
        if (!(state.email.length > 4 && state.email.length < 20)) {
            attention.email = true;
            valid = false;
        }

        if (valid) {
            // api signup here
        }
    }

    return {
        state,
        attention,
        postLogin,
        postSignup,
    }
});