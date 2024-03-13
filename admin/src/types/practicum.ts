import { Speciality } from '@/types/specisalities';

export enum PracticumScreenElement {
  Button = 'button',
  Text = 'text',
  Dropdown = 'dropdown',
  Image = 'image'
}

export type Side = 'left' | 'right';

export type ImageBlock = {
  id: number;
  type: PracticumScreenElement.Image;
  image: [File] | undefined;
  savedImage?: string;
  screenId?: number;
  order: number;
  side: Side;
};

export type DropdownItem = {
  id: number;
  title: string;
  text: string;
  order: number;
};

export type DropdownBlock = {
  id: number;
  type: PracticumScreenElement.Dropdown;
  screenId?: number;
  order: number;
  items: DropdownItem[];
  side: Side;
};

export type TextBlock = {
  id: number;
  type: PracticumScreenElement.Text;
  text: string;
  order: number;
  screenId?: number;
  side: Side;
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
  side: Side;
  order: number;
};

export type ScreenBlock = ImageBlock | DropdownBlock | ButtonBlock | TextBlock;

export const isButtonBlock = (block: ScreenBlock): block is ButtonBlock =>
  block.type === PracticumScreenElement.Button;

export const isImageBlock = (block: ScreenBlock): block is ImageBlock =>
  block.type === PracticumScreenElement.Image;

export const isDropdownBlock = (block: ScreenBlock): block is DropdownBlock =>
  block.type === PracticumScreenElement.Dropdown;

export const isTextBlock = (block: ScreenBlock): block is TextBlock =>
  block.type === PracticumScreenElement.Text;

export type ScreenInfo = {
  id: number;
  literature: string;
  literatureDescription: string;
  description: string;
  order: number;
  leftElements: ScreenBlock[];
  rightElements: ScreenBlock[];
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
  order: number;
  screen_button_block: {
    id: number;
    order: number;
    screen_number: number;
    side: Side;
    url: string;
    pdf_file: string;
    button_title: string;
    confirmation: boolean;
    fill_flag: boolean;
  }[];
  screen_text_block: {
    id: number;
    order: number;
    side: Side;
    text: string;
  }[];
  screen_image_block: {
    id: number;
    order: number;
    side: Side;
    image: string;
  }[];
  screen_popup_block: {
    id: number;
    order: number;
    side: Side;
    popup_points: {
      id: number;
      title: string;
      text: string;
      order: number;
    }[];
  }[];
};

export type BDPracticum = {
  id: number;
  description: string;
  title: string;
  image: string;
  image_desktop_810px?: string;
  image_desktop_1620px?: string;
  image_mobile_400px?: string;
  image_mobile_800px?: string;
  pacient_description: string;
  priority: number;
  screens: BDScreen[];
  speciality: number[];
};
