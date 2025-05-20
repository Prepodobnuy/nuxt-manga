export const useViewStore = defineStore("viewstate", () => {
  const viewSearch = ref(false);
  const viewLogin = ref(false);
  const viewSign = ref(false);
  const viewUtilMenu = ref(false);
  const viewCatalogMenu = ref(false);

  const toggleViewSearch = () => {
    viewSearch.value = !viewSearch.value;
  };
  const toggleViewLogin = () => {
    viewLogin.value = !viewLogin.value;
  };
  const toggleViewSign = () => {
    viewSign.value = !viewSign.value;
  };
  const toggleViewUtilMenu = () => {
    viewUtilMenu.value = !viewUtilMenu.value;
  };
  const toggleCatalogMenu = () => {
    viewCatalogMenu.value = !viewCatalogMenu.value;
  };
  const loginReverse = () => {
    toggleViewSign();
    toggleViewLogin();
  };

  const { mobile } = useViewportLE("tablet");

  return {
    viewSearch,
    viewLogin,
    viewSign,
    viewUtilMenu,
    viewCatalogMenu,
    toggleViewSearch,
    toggleViewLogin,
    toggleViewSign,
    toggleViewUtilMenu,
    toggleCatalogMenu,
    loginReverse,
    mobile,
  };
});
