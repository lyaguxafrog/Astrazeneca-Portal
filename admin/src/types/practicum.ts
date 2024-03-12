import { Speciality } from '@/types/specisalities';

export enum PracticumScreenElement {
  Button = 'button',
  Text = 'text',
  Dropdown = 'dropdown',
  Image = 'image'
}

export type ImageBlock = {
  id: number;
  type: PracticumScreenElement.Image;
  image: '';
  screenId?: number;
};

export type DropdownBlock = {
  id: number;
  type: PracticumScreenElement.Dropdown;
  screenId?: number;
  items: {
    title: string;
    text: string;
  }[];
};

export type TextBlock = {
  id: number;
  type: PracticumScreenElement.Text;
  text: string;
  screenId?: number;
};

export enum BtnType {
  Screen = 'Переход на экран',
  Link = 'Ссылка на страницу',
  File = 'PDF-файл'
}

export type ButtonBlock = {
  id: number;
  screenId: number;
  type: PracticumScreenElement.Button;
  title: string;
  btnType: null | BtnType;
  screenNumber?: number;
  link?: string;
  file?: [File];
  loadedFile?: string;
  withBg: boolean;
  confirmation: boolean;
};

export type ScreenBlock = ImageBlock | DropdownBlock | ButtonBlock | TextBlock;

export const isButtonBlock = (block: ScreenBlock): block is ButtonBlock =>
  block.type === PracticumScreenElement.Button;

export const isImageBlock = (block: ScreenBlock): block is ImageBlock =>
  block.type === PracticumScreenElement.Image;

export const isDropdownBlock = (block: ScreenBlock): block is DropdownBlock =>
  block.type === PracticumScreenElement.Dropdown;

export type ScreenInfo = {
  id: number;
  literature: string;
  literatureDescription: string;
  description: string;
  leftElements: ScreenBlock[];
  rightElements: ScreenBlock[];
  removing?: boolean;
};

export type Practicum = {
  id: number;
  priority: number;
  title: string;
  image: [File] | undefined;
  loadedImage: string;
  description: string;
  patientInfo: string;
  speciality: number[];
  screens: ScreenInfo[];
};

export type BDScreen = {
  id: number;
  literature: string;
  leterature_approvals_and_decodings: string;
  approvals_and_decodings: string;
  screen_button_block: {
    id: number;
    order: number;
    screen_number: number;
    side: string;
    url: string;
    pdf_file: string;
    button_title: string;
    confirmation: boolean;
    fill_flag: boolean;
  }[];
};

export type BDPracticum = {
  id: number;
  description: string;
  title: string;
  image: string;
  image_desktop_810px: string;
  image_desktop_1620px: string;
  image_mobile_400px: string;
  image_mobile_800px: string;
  pacient_description: string;
  priority: number;
  screens: BDScreen[];
  speciality: number[];
};
