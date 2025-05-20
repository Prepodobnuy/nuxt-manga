export const usePopupStore = defineStore("popupStore", () => {
  const message = ref<string | null>(null);

  const setMessage = (msg: string) => {
    message.value = msg;
  };

  const clearMessage = () => {
    message.value = null;
  };

  const timeOutMessage = (msg: string, timeout: number) => {
    setMessage(msg);
    setTimeout(() => {
      clearMessage();
    }, timeout);
  };

  return {
    setMessage,
    clearMessage,
    timeOutMessage,
  };
});
