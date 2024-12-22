<template>
    <div class="max-w-screen-xl mx-auto p-6 bg-teal-500">
        <div class="grid grid-cols-12 gap-4 mb-4">
            <!-- Blog Title -->
            <div class="col-span-9 bg-red-500">
                <h1 class="text-5xl font-bold text-gray-800">{{ blog.title }}</h1>
            </div>
            <!-- Additional Info -->
            <div class="col-span-3 text-sm text-gray-600 text-right">
                <p>Dec 19, 2024, 11:00 PM GMT+7</p>
                <p class="mt-1">Share this story</p>
                <p class="mt-1 font-semibold">17 Comments | 17 New</p>
                <p class="mt-1 text-gray-500">If you buy something from a Verge link, Vox Media may earn a commission.
                    See our ethics statement.</p>
            </div>
        </div>

        <!-- Blog Image -->
        <img :src="blog.image" :alt="blog.title" class="w-full h-full object-cover rounded-lg mb-6 shadow-lg" />

        <!-- Blog Content -->
        <div class="prose prose-lg max-w-none text-gray-700">
            <p v-html="blog.content"></p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BlogDetail',
    data() {
        return {
            blog: {
                title: "Asus ROG Zephyrus G16 (2024) review: an AMD upgrade",
                image: "https://duet-cdn.vox-cdn.com/thumbor/0x0:2040x1360/2400x1600/filters:focal(1239x649:1240x650):format(webp)/cdn.vox-cdn.com/uploads/chorus_asset/file/25696652/DSC_1121_Enhanced_NR.jpg",
                content: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Curabitur ac faucibus orci. Nulla facilisi. Proin tincidunt sem a 
            tortor sollicitudin, nec condimentum eros pretium.`,
            },
        };
    },
};
</script>

<style scoped>
.prose p {
    margin-bottom: 1rem;
}
</style>