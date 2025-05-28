export interface User {
  uuid: string;
  username: string;
  email: string;
  nickname: string | null;
  status?: string;
  about?: string;
  muted: boolean;
  moder: boolean;
  admin: boolean;
  translator: boolean;
  owns_translate_team: boolean;
  created_at: string;
}
