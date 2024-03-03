export enum PracticumScreenElement {
  Button = 'button',
  Text = 'text',
  Dropdown = 'dropdown',
  Image = 'image'
}

export type ImageBlock = {
  type: PracticumScreenElement.Image;
  image: '';
};

export type DropdownBlock = {
  type: PracticumScreenElement.Dropdown;
  title: string;
  text: string;
};

export type ScreenBlock = ImageBlock | DropdownBlock;

export const isImageBlock = (block: ScreenBlock): block is ImageBlock =>
  block.type === PracticumScreenElement.Image;

export const isDropdownBlock = (block: ScreenBlock): block is DropdownBlock =>
  block.type === PracticumScreenElement.Dropdown;

export type ScreenInfo = {
  id: number;
  literature: string;
  literatureDescription: string;
  description: string;
  elements: ScreenBlock;
};

export type Practicum = {
  id: number;
  title: string;
  image: [File] | null;
  description: string;
  patientInfo: string;
  speciality: string[];
  screens: ScreenInfo[];
};
