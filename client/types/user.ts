export interface User {
  uuid: string;
  username: string;
  email: string;
  nickname: string;
  status?: string;
  about?: string;
  muted: boolean;
  moder: boolean;
  admin: boolean;
  translator: boolean;
  created_at: string;
}
