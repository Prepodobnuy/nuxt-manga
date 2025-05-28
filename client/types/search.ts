import type { Title } from "./title";

export interface SearchPost {
  prompt: string | null;
  include_tags: number[];
  exclude_tags: number[];

  include_genres: number[];
  exclude_genres: number[];

  release_year_min: number | null;
  release_year_max: number | null;

  rate_min: number | null;
  rate_max: number | null;

  descending_order: boolean;
  sort_by_views: boolean;
  sort_by_rating: boolean;

  index: number;
}

export interface SearchResponse {
  end: boolean;
  titles: Title[];
}
