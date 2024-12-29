<template>
    <div class="max-w-screen-xl mx-auto p-6">
        <div class="grid grid-cols-12 gap-4 mb-2">
            <!-- Blog Title -->
            <div class="col-span-9">
                <h1 class="text-6xl font-bold text-gray-800">{{ blog.title }}</h1>
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
        <div class="mb-4">
            <h2 class="text-3xl">The AMD Strix Point CPU in the Zephyrus G16 gives this gaming laptop a battery life
                boost over the Intel version. Unfortunately, the price is also boosted.</h2>
        </div>
        <!-- Blog Image -->
        <img :src="blog.image" :alt="blog.title" class="w-full h-full object-cover rounded-lg mb-6 shadow-lg" />

        <div class="flex">
            <div class="max-w-3xl">
                <!-- Blog Content -->
                <div class="prose prose-lg max-w-3xl text-gray-700 p-4">
                    <h class="text-2xl">{{ blog.content }}</h>
                </div>

                <div class="text-gray-700 mt-6 mb-4 p-4">
                    <h class="text-xl">
                        {{ blog.content_x }}
                    </h>
                </div>

                <!-- Combined Card with Image and Content -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden mt-6">
                    <img src="https://cdn0.vox-cdn.com/hermano/verge/product/image/10340/DSC_1142.jpg"
                        alt="Additional Image" class="w-full h-128 object-cover" />
                    <div class="p-6 grid grid-cols-2 gap-4">
                        <!-- The Good Section -->
                        <div class="flex flex-col justify-between h-full bg-green-100 p-4 rounded-lg">
                            <h3 class="text-lg font-bold text-gray-800 mb-2">The Good</h3>
                            <ul class="list-disc list-inside text-gray-700">
                                <li>Above-average battery life for a gaming laptop</li>
                                <li>Thin and light</li>
                                <li>Exceptional screen and speakers</li>
                                <li>All-around good build quality with little flex</li>
                            </ul>
                            <div class="mt-auto">
                                <button
                                    class="px-4 py-2 bg-green-600 text-white font-bold rounded-lg shadow hover:bg-green-500 w-full">
                                    $2100 at Best Buy
                                </button>
                            </div>
                        </div>
                        <!-- The Bad Section -->
                        <div class="flex flex-col justify-between h-full bg-red-100 p-4 rounded-lg">
                            <h3 class="text-lg font-bold text-gray-800 mb-2">The Bad</h3>
                            <ul class="list-disc list-inside text-gray-700">
                                <li>Expensive, undercut by Asus’ own offerings</li>
                                <li>Still runs hotter than competitors</li>
                                <li>Performance lags behind laptops with similar specifications</li>
                                <li>RGB lighting underwhelming for a laptop this expensive</li>
                            </ul>
                            <div class="mt-auto">
                                <button
                                    class="px-4 py-2 bg-red-600 text-white font-bold rounded-lg shadow hover:bg-red-500 w-full">
                                    $2080 at Asus
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="text-gray-700 mt-6 mb-4 p-4">
                    <h class="text-lg">
                        {{ blog.content_y }}
                    </h>
                </div>

                <div class="text-gray-700 p-4">
                    <h class="text-lg">
                        {{ blog.content_z }}
                    </h>
                </div>
                <div class="text-gray-700 mb-4 p-4">
                    <h class="text-lg">
                        {{ blog.content_r }}
                    </h>
                </div>

                <div class="max-w-full mb-4 p-4">
                    <h2 class="text-xl font-bold text-gray-800 mb-4">Watch This Video</h2>
                    <div class="aspect-w-16 aspect-h-9">
                        <iframe width="100%" height="315" src="https://www.youtube.com/embed/lPSxGmrqJzA"
                            title="YouTube video player" frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowfullscreen></iframe>

                    </div>
                </div>
                <div class="text-gray-700 mb-4 p-4">
                    <h class="text-lg">
                        {{ blog.content_f }}
                    </h>
                </div>
                <!-- Product Features Card -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden mt-6">
                    <div class="p-6">
                        <h3 class="text-xl font-bold text-gray-800 mb-4">Product Features</h3>
                        <ul class="list-disc list-inside text-gray-700">
                            <li>Powered by the latest AMD Ryzen AI 9 HX 370 CPU</li>
                            <li>Exceptional 2560 x 1600 OLED display with 240Hz refresh rate</li>
                            <li>Ultra-lightweight design, only 3.99 pounds</li>
                            <li>Improved battery life, up to 12 hours with moderate use</li>
                            <li>RGB backlighting with customizable effects</li>
                            <li>Wi-Fi 7 for faster and more reliable connectivity</li>
                            <li>Multiple storage options: 1TB, 2TB SSD</li>
                            <li>Enhanced cooling system for quieter and more efficient operation</li>
                            <li>Thin, premium aluminum chassis</li>
                        </ul>
                    </div>
                </div>

            </div>
            <!-- List of Other Blog Posts -->
            <div class="max-w-sm ml-6">
                <h2 class="text-xl font-bold text-gray-800 mb-4">Most Popular</h2>
                <div v-for="(item, index) in blogs" :key="index" class="mb-4">
                    <div class="bg-gray-100 p-4 rounded-lg shadow">
                        <h3 class="font-semibold text-gray-800">{{ item.title }}</h3>
                        <p class="text-gray-600 text-sm mt-2">{{ item.date }}</p>
                    </div>
                </div>
            </div>
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
                content_f: "Whichever processor and graphics card is inside, using the G16 is a rock-solid experience. There’s very little chassis flex except for the plate in the dead center of the keyboard, the lid lifts easily with a single finger, and screen wobble is minimal. But the 2560 x 1600, 240Hz OLED ROG Nebula Display steals the show. Thanks to the excellent motion clarity, color accuracy, and contrast, it’s just about the best screen you can find on a gaming laptop. The smaller Asus ROG Zephyrus G14 uses a 2880 x 1800 OLED panel, but it’s only 120Hz.",
                content_r: 'I have a solid basis for comparing the two G16s here. In search of a portable work machine I could also game on, I ditched my desktop and bought the Intel version of the G16, with an RTX 4070 and 16GB of RAM, in August. Since then, I’ve used it not only to work at home and in coffee shops but also to play all the games I’d normally play on my tower.',
                image: "https://duet-cdn.vox-cdn.com/thumbor/0x0:2040x1360/2400x1600/filters:focal(1239x649:1240x650):format(webp)/cdn.vox-cdn.com/uploads/chorus_asset/file/25696652/DSC_1121_Enhanced_NR.jpg",
                content: `Asus overhauled its ROG Zephyrus gaming laptops in 2024, giving them sleek, 
                aluminum bodies and brilliant OLED screens. The Intel version of the ROG Zephyrus G16 looked like a potential MacBook Pro killer when it launched in February; it is thin, light, and powerful, but the Core Ultra 9 185H processor hampers battery life. Now that Asus has reissued the G16 with the latest flagship CPU from AMD, it has finally become an all-rounder with enough battery life to tote to the office..`,
                content_x: 'This version of the Zephyrus G16 has the same Ryzen AI 9 HX 370 CPU that powers Asus’ Zenbook S 16 to great effect. The better integrated graphics and improvements in efficiency and raw horsepower over Intel’s mobile Meteor Lake processors make the AMD model the clear winner. If only it weren’t so dang expensive. ',
                content_y: 'Our $2,300 review unit, with an Nvidia RTX 4070 mobile GPU, is one of four G16 variants with the Ryzen AI 9 HX 370 CPU. There’s another 4070 model in white, with 32GB of RAM and 2TB of storage for $2,300, while the least expensive version is $1,900 with an RTX 4060, 16GB of RAM, and 1TB of storage. More GPU power is only available on Intel models, with an RTX 4080 option at $2,700 and an RTX 4090 for $3,300. RAM is soldered to the motherboard, so it’s important to consider before purchasing',
                content_z: 'Apart from the processor, and the jump to Wi-Fi 7 from Wi-Fi 6e, the AMD version of the G16 is nearly identical to the Intel version. Both use the same 0.59-inch-thick unibody aluminum chassis, ports, and 200-watt charging brick; the only visible difference is the Copilot key on the AMD model in place of the right-hand Ctrl key. The AMD version is also an ounce lighter at a scant 3.99 pounds. '
            },
            blogs: [
                {
                    title: "Google’s counteroffer to the government trying to break it up is unbundling Android apps",
                    date: "Dec 21, 2024"
                },
                {
                    title: "2025 will be the year of the smart lock",
                    date: "Dec 19, 2024"
                },
                {
                    title: "Three of the biggest US banks are facing a lawsuit for ‘widespread fraud’ on Zelle",
                    date: "Dec 18, 2024"
                },
                {
                    title: "ModRetro Chromatic review: an arms dealer’s Game Boy is among the best ever made",
                    date: "Dec 17, 2024"
                },
                {
                    title: "Qualcomm wins a legal battle over Arm chip licensing",
                    date: "Dec 16, 2024"
                }
            ]
        };
    },
};
</script>

<style scoped>
.prose p {
    margin-bottom: 1rem;
}
</style>
