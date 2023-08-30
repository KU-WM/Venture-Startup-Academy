import { atom } from "recoil";

const waiting = atom({
    key: 'waiting',
    default: [],
});

export {waiting};