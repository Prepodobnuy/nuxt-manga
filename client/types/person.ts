export interface Person {
  id: number;
  person_id: number;
  created_user_uuid: string;
  name_ru: string;
  name_en: string;
  name_jp: string;
  name_an: string | null;
  description: string | null;
  approved: boolean;
  approved_at: string | null;
  approved_user_uuid: string | null;
  created_at: string;
}

export interface PersonFull {
  id: number;
  user_published_uuid: string;
  created_at: string;
  meta: Person;
  unapproved_metas: Person[];
}

export interface PersonPost {
  name_ru: string;
  name_en: string;
  name_jp: string;
  name_an: string | null;
  description: string | null;
}
