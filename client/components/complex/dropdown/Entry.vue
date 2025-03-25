<template>
  <li>
    <slot></slot>
  </li>
  </template>
  
  <style lang="scss" scoped>
  
  li {
    cursor: pointer;

    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    
    gap: var(--row-gap-0);
    user-select: none;
  
    min-width: 140px;
    height: var(--input-height);
    padding: var(--input-padding);
    border-radius: var(--input-borrad);
  
    transition: background-color 0.22s;
  
    font-size: 80%;

    &:active {
      background-color: var(--color-primary-background-8);
    }
  }
  
  </style>
  