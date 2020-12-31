<template>
  <button v-on:click="mark = mark + '!'">Hello {{ name }} {{ mark }}</button>
</template>

<script>
export default{
  props: ['name'],
  data: function () {
    return {
      mark: '!'
    }
  },
}
</script>
