export interface Title {
  id: number;
  title_id: number;
  title_ru: string;
  title_en: string;
  title_jp: string;
  title_an: string | null;
  release_year: string;
  description: string | null;
  author_id: number;
  artist_id: number;
  publisher_id: number;
  tags: number[];
  genres: number[];
  approved: boolean;
  approved_at: string | null;
  approved_user_uuid: string | null;
  created_user_uuid: string;
  created_at: string;
}

export interface TitlePost {
  title_ru: string;
  title_en: string;
  title_jp: string;
  title_an: string | null;
  release_year: string;
  description: string | null;
  author_id: number;
  artist_id: number;
  publisher_id: number;
  tags: number[];
  genres: number[];
}
