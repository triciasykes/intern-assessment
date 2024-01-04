export interface User {
  id: number;
  first_name: string;
  last_name: string;
  dob: string;
  email: string;
}

export interface Contact {
  id: number;
  first_name: string;
  last_name: string;
  dob: string;
  email: string;
  connected_to: number;
  avatar: string;
}
