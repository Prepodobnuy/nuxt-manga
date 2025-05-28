export interface TranslateTeamPostScheme {
  description: string | null;
  title: string;
}

export interface TranslateTeamMemberScheme {
  uuid: string;
  team_id: number;
  accepted: boolean;
}

export interface TranslateTeamScheme {
  id: number;
  owner_uuid: string;
  title: string;
  description: string | null;
  approved: boolean;
  accepted_members: TranslateTeamMemberScheme[];
  unaccepted_members: TranslateTeamMemberScheme[];
}
